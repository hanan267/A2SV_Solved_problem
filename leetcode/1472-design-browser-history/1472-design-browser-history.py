class Node:
    def __init__(self, url="", prev=None, next=None):
        self.url = url
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.currNode = Node(url=homepage)

    def visit(self, url: str) -> None:
        new_Node = Node(url)
        self.currNode.next = new_Node
        self.currNode.next.prev = self.currNode
        self.currNode = self.currNode.next

    def back(self, steps: int) -> str:
        while self.currNode.prev and steps > 0:
            self.currNode = self.currNode.prev
            steps -= 1
        return self.currNode.url

    def forward(self, steps: int) -> str:
        while self.currNode.next and steps > 0:
            self.currNode = self.currNode.next
            steps -= 1
        return self.currNode.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)