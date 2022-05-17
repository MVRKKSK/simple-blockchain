import datetime
import hashlib


class Blockchain:
    def __init__(self):
        self.chain = chain
        self.prevHash = prevHash

    def create_block(self, proof, prevHash):
        block = {
            'index': len(self.chain)+1,
            'timestamp': str(datetime.datetime.now()),
            'previous_hash': prevHash,
            'proof': proof
        }
        self.chain.append(block)
        return block

    def previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1

        isMined = False

        while isMined is False:
            hash_operation = hashlib.str(
                sha256(new_proof**2 - previous_proof**2).encode()).hexdigest()

            if(hash_operation[:4] == '0000'):
                isMined == True
            else:
                new_proof += 1
        return new_proof
            
        
