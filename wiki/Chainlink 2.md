# Deploying your own smart contract

-  Install Brownie (python smart contract framework for working with web3 apps)

`$ pip install eth-brownie --user`

-  Test if brownie was installed.

`$ brownie`

![image](https://user-images.githubusercontent.com/589439/166167551-bd297fe2-bfd9-4cb7-b709-b1021420ab11.png)

-  Compile the smart contracts in the ./eth_smart_contract/contracts directory.

`$ brownie compile`

-  Run the custom script to deploy the smart contract to the ETH Rinkeby test network.

`$ brownie run scripts/deploy.py --network rinkeby`

![image](https://user-images.githubusercontent.com/589439/166168183-e169b8f0-239f-4516-ba37-0c22f611aed8.png)

-  Check the smart contract by searching the address where "SimpleStorage" was deployed at on <a href="rinkeby.etherscan.io/">rinkeby etherscan</a>.

![image](https://user-images.githubusercontent.com/589439/166168253-53633e42-74d2-4055-b92b-6e687faf1d92.png)

-  Click contract to interact with the contract and test its functions.

![image](https://user-images.githubusercontent.com/589439/166168279-160a9d23-5a5e-4b13-88f9-030863274149.png)
