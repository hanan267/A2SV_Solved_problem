class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = collections.defaultdict(int)

        for domain in cpdomains:
            count, site = domain.split()
            #print(count, site)

            count = int(count)
            site = site.split(".")
            for i in range(len(site)):
                counts[".".join(site[i:])] += count
            

        return [f"{rep} {site}" for site, rep in counts.items()]
       

        