// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract SimpleStorage {
    // Contents of our contract simple storage.

    address public owner;
    int256 public storage_count;

    constructor() public {
        storage_count = 0;
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    function update_count(int256 count) public payable onlyOwner {
        storage_count = storage_count + count;
    }
}
