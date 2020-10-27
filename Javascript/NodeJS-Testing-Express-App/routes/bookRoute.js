const router = require('express').Router()


// getting the Book Controller
const bookController = require('../controller/bookController')

router.get('/', bookController.getAllBooks)

router.get('/:bookId', bookController.getABook)

router.post('/', bookController.addBook)

router.delete('/delete/:bookId', bookController.deleteBook)

// router.patch('/:bookId')

module.exports = router