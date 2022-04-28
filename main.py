import fastapi as _fastapi
import yennengaBlockchain as _blockchain

blockchain = _blockchain.Blockchain()
app = _fastapi.FastAPI()


# endpoint to mine a block
@app.post("/mine_yennengaBlockchain_block/")
def mine_yennenga_block(data: str):
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400,
            detail="The Yennenga Blockchain is invalid"
        )
    block = blockchain.mine_block(data=data)
    
    return block


# endpoint to return the entire blockchain
@app.get("/yennenga_blockchain/")
def get_yennenga_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, 
            detail="The Yennenga Blockchain is invalid"
        )
    chain = blockchain.chain
    
    return chain


# endpoint returns the previous block
@app.get("/yennengaBlockchain_previous_block/")
def yennenga_previous_block():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(
            status_code=400, detail="The Yennenga Blockchain is invalid"
        )
    return blockchain.get_previous_block()


# endpoint to see if the blockchain is valid
@app.get("/validate_yennengaBlockchain/")
def is_yennenga_blockchain_valid():
    
    return blockchain.is_chain_valid()