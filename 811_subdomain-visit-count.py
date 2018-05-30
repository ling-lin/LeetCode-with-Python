class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        result = {}
        re = []
        for i in range(len(cpdomains)):
            cnt, web = cpdomains[i].split(' ')
            webs = web.split('.')
            for j in range(len(webs)):
                webname = '.'.join(webs[j:])
                if webname not in result:
                    result[webname] = int(cnt)
                else:
                    result[webname] += int(cnt)
        for i in result:
            t = [str(result[i]), i]
            re.append(' '.join(t))
        return re 
