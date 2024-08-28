class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited=[False]*len(rooms)
        keys=[0]
        visited[0] = True
        count=1

        while keys:
            current_room=keys.pop()
            for key in rooms[current_room]:
                if not visited[key]:
                    visited[key]=True
                    keys.append(key)
                    count+=1
                    if count==len(rooms):
                        return True

        return False            
