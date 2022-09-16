// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract MyNFT is ERC721, ERC721Enumerable, ERC721URIStorage, Ownable {

     // ===== Property Variables ===== //
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;
    // uint256 public MINT_PRICE = 0.05 ether;
    uint256 public MAX_SUPPLY = 100000;

    constructor() ERC721("BDNFT", "BDFT") {
        // Start token ID at 1. By default it starts at 0.
        _tokenIdCounter.increment();
    }


    // ===== Minting Functions ===== //
    // Allow All Users to mint NFT
   
    function safeMint(address to, string memory uri) public { 
        require(_tokenIdCounter.current() <= MAX_SUPPLY, "Sorry All NFTs has been minted");
        // Check if ether value is correct
        // require(msg.value >= MINT_PRICE, "Not enough ether sent.");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, uri);
    }

    function tokenURI(uint256 tokenId) public view override(ERC721, ERC721URIStorage) returns (string memory) {
        return super.tokenURI(tokenId);
    }

    /*

    function withdraw() public onlyOwner() {
        require(address(this).balance > 0, "Balance is zero");
        payable(owner()).transfer(address(this).balance);
    }

    function _baseURI() internal pure override returns (string memory) {
        return "ipfs://<baseURI>/";
    }

    */

    // The following functions are overrides required by Solidity.

    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function supportsInterface(bytes4 interfaceId) public view override(ERC721, ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}

/*
  safeMint: uri => IPFS NFT metadata CID
  EX: ipfs://QmTyuUnyiAbAvdiqhyGW8hTjDgBqNHJmncF1FUkMNrfrzC
  contract => 0x30552EC6D02d459f390B7EB725791066859e655A
*/
