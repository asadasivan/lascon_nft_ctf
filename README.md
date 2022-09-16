Lascon 2022 NFT CTF Challenge
=============================

## Introduction
This project contains information on how to create and deploy a Ethereum smart contract using solidity programming language and also minting a NFT token. 

## Getting Started
Checkout the project and start using it.

## Prerequisites
1. Download remix IDE: https://remix.ethereum.org (You can also use VisualStudio code, but the setup is complex)
2. Setup metamask on your chrome/firefox browser: https://metamask.io/
3. Create a File Base account: https://console.filebase.com
4. Create an Etherscan account: https://etherscan.io/login
5. Install remix IDE plugin: Flattener to publish the source to Etherscan
6. Alchemy web3 development platform (optional): https://dashboard.alchemy.com/   

## Get familiarized with the following:
1. NFT (Non-fungible token):
   * NFT Images are not stored in the blockchain as it is expensive. They are usually stored in ipfs.  
2. Smart contract
    * Openzeppelin contains examples of different smart contracts using the Solidity programming language.
    * https://docs.openzeppelin.com/contracts/4.x/
    * Familiarize essential functions like minting, burning, transferring, and ownership information.
3. Etherscan: 
   * Etherscan is a Blockchain Explorer for Ethereum. Etherscan allows you to search through transaction history, blocks, wallet addresses, smart contracts for ERC-20 tokens, and other on-chain data.
4. InterPlanetary File system (IPFS)
   * A decentralized and collaborative webpage delivery technology
   * https://ipfs.io/	    	  
5. Create a smart contract, metadata.json file, and the image that you want to be created as an NFT token. 

## Upload files to File Base:
   1. Login to File Base (https://console.filebase.com/) > Buckets > Create bucket
   2. Provide a unique name for your bucket. EX: nft-demo-assets
   3. Select Storage Network: IPFS
   4. Upload the image which you want to be created as an NFT token.
   5. Copy the IPFS Gateway URL
   6. Open the metadata file and update the "image" with IPFS Gateway URL. EX: https://ipfs.filebase.io/ipfs/<IPFS CID\>
   7. Upload metadata.json to File Base.
   8. Copy the IPFS CID
   9. Smart contract functions like safeMint and opensea.io marketplace require ipfs with the following format: ipfs://\<CID\> 
   
## Use remixIDE to deploy and test smart contract:
   1. Test your smart contract using remixVM to ensure there are no bugs. 
   2. Perform actions like deploying contract and reading/writing from contract using the functions provided in the smart contract.
   3. Open remixIDE 
   4. Compile the .sol source file
   5. Remix IDE > Deploy & Run Transactions > RemixVM Environment
   6. Click the Deploy button to deploy the contract
   7. Under Deployed contracts > Test functions like safeMint, tokenURI, etc.
   8. safeMint function is used to mint NFT:
      * Enter the wallet address (Account address)
      * Enter uri: ipfs://\<CID\> 
      *  Click transact button
   9. tokenURI function returns the URI of metadata file:
      * Enter 1 as in our smart contract, tokenId starts from 1 instead of 0.
      * Click the call button 
      * Output will be as follows: ipfs://\<IPFS CID\>
   10. Open the browser and go to https://ipfs.io/ipfs/<IPFS CID\>

## Deploy smart contract to Polygon testnet network instead of Ethereum mainnet network:
   1. Add Polygon Mumbai Testnet Network to metamask.
   2. Use Chainlist (https://chainlist.org/) to connect to the Polygon Mumbai Testnet network to your metamask wallet
   3. Testnet networks are mainly used for testing purposes.
   4. Use faucet to get free cryptocurrency to test:
      * Go to https://faucet.polygon.technology
      * Paste wallet address from metamask > Click Submit button
      * You will see a free MATIC token in your metamask wallet that you can use to pay for gas
   5. Open remixIDE 
   6. Compile the .sol source file
   7. Remix IDE > Deploy & Run Transactions > Environment > select Injected Provider for connecting Remix to an injected web3 provider like Metamask.	
   8. Ensure the metmask account is connected to the Mumbai Testnet network.
   9. Click the Deploy button to deploy the contract 
   
## Verify and Publish in Etherscan Testnet (optional):
   1. Publishing your code allows you to interact with your smart contract directly from Etherscan. 
   2. To verify and publish your code from remix IDE to Etherscan, use the remix plugin: Flattener
   3. Deploy the original file (unflattened)
   4. Use Flattener in remixIDE to create a flattened file
   5. Go to Etherscan Testnet. EX: https://mumbai.polygonscan.com/address
   6. Search for the contract and go to the contract tab and click Verify and Publish
   7. Paste the single flattened file.
   8. After verification, there will be options for reading/writing to the contract.
   9. Ensure metamask is connected to the testnet site. 
   
## Mint NFT using testnet:
   1. Open metamask > Copy Transaction ID (Contract Deployment)
   2. Go to Etherscan Testnet and search for the transaction ID 
   3. Click Contract created address > Contract tab
   4. Click Write Contract > safeMint
   5. Enter the wallet address and uri > Write
   6. Click Read Contract > tokenURI
   7. Enter tokenID > 1 > Click Query button
   8. Follow prompts in metamask and pay gas fees using free coins provided by the faucet. 
   9. Go to https://testnets.opensea.io
   10. Click profile > Connect testnet opensea with metamask > Follow the prompts
   11. Your profile page provides you with a list of all NFTs created and collected.

## Rinkeybe testnet network
   1. Faucet is a way to get free cryptocurrency to test.
   2. Rinkeybe faucet: https://faucets.chain.link/ 
   3. Block explorer: https://rinkeby.etherscan.io/
   4. Testnet NFT Marketplace: https://testnets.opensea.io/account 
	
## Polygon testnet network
   1. Use Polygon Mumbai Test Network instead of Ethereum
   2. Polygon faucet: https://faucet.polygon.technology
   3. Block explorer: https://mumbai.polygonscan.com/
   4. Testnet NFT Marketplace: https://testnets.opensea.io/account	
	   
## Mainnet
   1. Block explorer: https://etherscan.io/
   2. IPFS file storage: https://ipfs.io/
   3. NFT marketplace (Opensea): https://opensea.io/learn/what-are-nfts
   4. List of EVM networks: https://chainlist.org/
   5. https://dappradar.com/nft/collections
      * Click Top Collections > Click Ethereum
	   
## IDE/Playground
   1. Remix IDE: https://remix.ethereum.org
   2. EVM playground: https://www.evm.codes/playground	
	
## Pinata:
   1. Pinata is similar to FireBase. 
   2. Pin your content to IPFS with Pinata 
   3. https://app.pinata.cloud/
   4. EX: https://gateway.pinata.cloud/ipfs/\<CID\>
   5. Upload files/folder, and CID will be the baseURI
   6. Folder: https://gateway.pinata.cloud/ipfs/<IPFS CID\>/
   7. File: https://gateway.pinata.cloud/ipfs/<IPFS CID\>?filename=1.jpg	
	
## References:
   1. Solidity: https://soliditylang.org/
   2. https://docs.alchemy.com/docs/how-to-develop-an-nft-smart-contract-erc721-with-alchemy#create-a-free-alchemy-account
   3. Ethereum smart contract best practices: https://consensys.github.io/smart-contract-best-practices/

## Getting Help
contact Arunkumar Sadasivan <contact.arunsec@gmail.com>

## Contributing
1. Fork it
2. Commit your changes 
3. Push to the branch
4. Create new Pull Request

## Issues
To report issues, bugs and enhancements requests, use the issue tracker. 
