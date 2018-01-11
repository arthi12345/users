 def writeLogs(self,out,msg):
        svnInfo = SvnInfo()
        file = open(config.logfilePath+"log.txt", "w")
        file.write(out)
        file.close()
        attach_files=[]
        attach_files.append(config.logfilePath+"log.txt")
        (status,versionInfo) = svnInfo.getAll({})
        logger.info("vesrion" + str(versionInfo))
        version = versionInfo["data"][0]["version"]
        #version="222"
        body = "Svn Version : "+version+"<br>Updated Time : "+time.strftime("%c")+"<br>"
        body = body+"Please find below attached log."
        return sendemail(config.toUsersList,msg,body,attach_files)

