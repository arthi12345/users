def hashInfo(self,id):
        print "id: %s"%id
        if(id=="dummy"):
            (status ,out, err) = execution(config.gitInfo)
        else:
            cmd = "cd /salt/states/base/repo/smartrecon; git show --name-only " + id
            (status, out, err) = execution(cmd)
        print "status: %s"%status
        print "out: %s"%out
        print "err: %s"%err
        print "cmd o/p"+out
        #return True,out  
        return True,{"output":out}
