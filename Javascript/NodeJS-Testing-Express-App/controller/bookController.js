const fs = require('fs')


const path = './Dummy Book Data/data.json'

const fileReader = async() => {

    return new Promise((resolve, reject) => {
        fs.readFile(path, 'utf8', (err, data) => {
            if (err) {
                // console.log('Failed to fetch Data: ', err)
                reject(err)
            } else {
                resolve(JSON.parse(data))
            }



        })
    })

}


const filerWriter = async(data) => {


    return new Promise((resolve, reject) => {
        fs.writeFile(path, data, err => {
            if (err) {
                console.log('Failed to write Data: ', err)
                reject(err)
            }


            resolve("File written successfully")

        })
    })

}



const getAllBooks = async(req, res, next) => {


    try {
        const result = await fileReader()
            // console.log(result)


        if (result instanceof Error) {
            throw result
        }

        res.status(200).json({
            data: result.Books
        })
    } catch (err) {
        return res.status(404).json({
            Error: err.message
        })
    }


}


const getABook = async(req, res, next) => {

    try {
        const result = await fileReader()
            // console.log(result)
        if (result instanceof Error) throw result


        const id = req.params.bookId
        const books = result.Books

        const myBook = books.filter(b => b.id === id)[0]

        if (!myBook) throw Error("Book Not Found")


        res.status(200).json({
            Book: myBook
        })

    } catch (err) {
        res.status(404).json({
            message: err.message
        })
    }




}




const addBook = async(req, res, next) => {


    try {

        const { id, title, author } = req.body
        if (id === undefined || title === undefined || author === undefined) throw Error('Object Not Completely Defined')

        const book = { id, title, author }

        const getBooks = await fileReader()

        getBooks.Books.push(book)

        const result = await filerWriter(JSON.stringify(getBooks, null, 2))
        if (result instanceof Error) throw result


        res.status(200).json({
            message: "Successfully Added Book"
        })
    } catch (err) {
        const message = err.message
        res.status(404).json({
            Error: message,
            message: "Failed to post book"
        })
    }

}

const deleteBook = async(req, res, next) => {
    const id = req.params.bookId

    try {
        const getBooks = await fileReader()
        getBooks.Books = getBooks.Books.filter(b => b.id !== id)

        const result = await filerWriter(JSON.stringify(getBooks, 2, null))
        if (result instanceof Error) throw result


        res.status(200).json({
            message: "Successfully Deleted Book"
        })


    } catch (err) {
        res.status(404).json({
            Error: result.message,
            message: "Failed to post book"
        })
    }


}


module.exports = { getAllBooks, getABook, addBook, deleteBook }