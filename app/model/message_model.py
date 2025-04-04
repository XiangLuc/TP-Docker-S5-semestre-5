class Message:
    
    def __init__(self, id: int, message: str):
        self.id = id
        self.message = message
        
        
    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message
        }