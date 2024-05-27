# Flash
Flash memory is organized into blocks and pages, with pages being the smallest unit that can be written to, and blocks being the smallest unit that can be erased.

## quick specifications

Flash memory is made of **blocks**, which are the **smallest unit that can be erased**. Remember that, it’s really important.
Each block contains a number of **pages**, which are the **smallest unit that can be programmed** (i.e. written to).
The important bit here is that program operations (i.e. writes) take place to a page, which might typically be 8-16KB in size, while erase operations take place to a block, which might be 4-8MB in size. Since a block needs to be erased before it can be programmed again (*sort of, I’m generalizing to make this easier), all of the pages in a block need to be candidates for erasure before this can happen.

## Writing
When you write data to a flash memory page, any bits that need to be changed from '1' to '0' can be written directly. However, bits cannot be changed from '0' to '1' without an erase.

## Page State
Once a page is written, if any additional changes are needed (including setting any '0' bits back to '1'), the entire block containing that page must be erased first. This is because flash memory does not allow bit-wise erasure—only whole blocks can be erased.

## Program Erase Cycle
Program-Erase Cycles: Each page within a flash memory block can be written to and erased a certain number of times before the reliability of the memory degrades. This is known as the program-erase cycle.

## Write Amplification:
To update a single page, data from other pages in the same block may need to be copied to a new block, the original block erased, and then all the data (including the updated page) written back to the clean block. This process, known as write amplification, is necessary because individual pages cannot be erased.
