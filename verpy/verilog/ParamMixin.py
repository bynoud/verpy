
from .Net import Parameter

def _isGlobal(x):
    return x.ntype == 'parameter'
def _isLocal(x):
    return x.ntype == 'localparam'
def _isParam(x):
    return _isGlobal(x) or _isLocal(x)

class ParamMixin(object):
    def paramInit(self, paramList):
        self._params = paramList

    def _newParam(self, kw, name, val):
        p = self._params.new(Parameter, name=name, ntype=kw)
        p.val = val
        return p

    def newParam(self, name, val):
        return self._newParam('parameter', name, val)

    def newLocalparam(self, name, val):
        return self._newParam('localparam', name, val)

    # Use to manual overwrite paramenter which include unknow-value (ex:function call)
    def overwriteParam(self, params):
        for (p,v) in params.iteritems():
            assert isinstance(self._params[p], Parameter)
            self._params[p].val = v

    @property
    def parameters(self):
        try: return self._paramresolved
        except:
            #r = {}
            #print("--- get param")
            #for x in self._params.filter(_isParam):
            #    print("-- %s = %s" % (x.name, x.val))
            #    r[x.name] = x.val
            #return r
            return {x.name : x.val for x in self._params.filter(_isParam)}

    def defparams(self, defp):
        par = self._params.filter(_isGlobal)
        if isinstance(defp,list):
            for k in range(len(defp)):
                par[k].val = defp[k]
        else:
            for (k,v) in defp.iteritems():
                par[k].val = v

    def elaborate(self, defparams=None):
        from .AstEvaluation import eval_expression
        if defparams: self.defparams(defparams)
        resolved = True
        params = self.parameters
        ## first try convert all to integer
        #for (k,v) in params.iteritems():
        #    try: params[k] = int(v)
        #    except: resolved = False
        #if not resolved:
        #    for i in range(100):
        #        resolved = True
        #        for (k,v) in params:
        #            if not isinstance(v, int):
        #                try: params[k] = eval_expression(v, self.params)
        #                except: resolved = False
        #        if resolved: break
        for i in range(100):
            resolved = True
            for (k,v) in params.iteritems():
                try: params[k] = eval_expression(v, params)
                except Exception,e:
                    resolved = False
            if resolved: break
        if not resolved:
            raise Exception("Cannot resolve parameter dependence: %s" % params)
        self._paramresolved = params


