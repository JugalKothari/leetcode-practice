
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        global_vis=[False]*V
        local_vis=[False]*V
        
        def check_cyclic(node, adj, global_vis, local_vis):
            if not global_vis[node]:
                global_vis[node]=True
                local_vis[node]=True
                
                for child in adj[node]:
                    if check_cyclic(child, adj, global_vis, local_vis):
                        return True
                    elif local_vis[child]:
                        return True
                local_vis[node]=False
            return False
                
        
        for starting in range(V):
            if not global_vis[starting] and check_cyclic(starting, adj, global_vis, local_vis):
                return True
        return False
