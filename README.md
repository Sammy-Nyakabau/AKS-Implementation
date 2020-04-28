# AKS-Implementation
Web UI implementation of the [AKS Primality Testing Algorithm](https://en.wikipedia.org/wiki/AKS_primality_test) using HTML, CSS, Bootstrap and Brython

## Design

The User Interface was designed using HTML, CSS and [Bootstrap 4](https://getbootstrap.com/). A user types in the number they want to test in the **Input Box** and press the **Check** Button. The result of the operation will be output on the **Output Box**. To test a different number, the user has an option to press the **Reset** Button which clears both the **Input Box** and the **Output Box**.

### Example

![Testing 31](https://i.ibb.co/BPcNwnj/image.png)


## Implementation

The initial implementation was done in [python 3](https://www.python.org/). The file [aks_final.py](https://github.com/Sammy-Nyakabau/AKS-Implementation/blob/master/aks_final.py) contains the code in python. However, since python cannot be run in the browser, I made use of [Brython](https://brython.info/index.html) which lets you write Python in script tags in exactly the same way you write JavaScript. It has a `document object` for interacting with the DOM which makes it possible to change the functionality of buttons and text boxes. The file [index.html](https://github.com/Sammy-Nyakabau/AKS-Implementation/blob/master/Index.html) contains the basic structure of Web UI plus required files for Bootstrap and Brython functionality. The file [style.css](https://github.com/Sammy-Nyakabau/AKS-Implementation/blob/master/style.css) contains CSS code to make the Web UI more appealing.

## Final Notes

The algorithm is not as fast as compared with other primality testing algorithms. Coupled with that is the use of python as a programming language which is not known for its speed. Using Brython to compile the python code into javascript also adds to the speed overhead. Thus, for testing purposes, make use of the [aks_final.py](https://github.com/Sammy-Nyakabau/AKS-Implementation/blob/master/aks_final.py). The Web UI is only responsive for numbers < 100. Above that, users will experience a massive lag before they can see an answer on the **Output Box**. 

___

## Credits

The following people are responsible for the design and implementaion of this project
1. Jenish Raj
2. Nidup Dorji
3. Sammy Nyakabau
4. Stuti Khandelwal
    
