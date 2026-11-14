class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        accountNames = {}
        rank = {}
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                node = account[i]
                accountNames[node] = name
                rank[node] = 0
                parent[node] = node
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(a, b):
            ra = find(a)
            rb = find(b)
            if ra == rb:
                return 
            
            if rank[ra] < rank[rb]:
                parent[ra] = rb 
            elif rank[rb] < rank[ra]:
                parent[rb] = ra
            else:
                parent[ra] = rb 
                rank[rb] += 1
        for account in accounts:
            a1 = account[1]
            for i in range(2, len(account)):
                a2 = account[i]
                union(a1, a2)
        
        finalAccounts = defaultdict(list)
        for account in sorted(parent.keys()):
            root = find(account)
            finalAccounts[root].append(account)
        res = []
        for root in finalAccounts.keys():
            account = [accountNames[root]]
            account += finalAccounts[root]
            res.append(account)

        return res


            
        
        


        