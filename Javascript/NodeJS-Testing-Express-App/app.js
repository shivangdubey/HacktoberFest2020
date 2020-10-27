const express = require('express')
const app = express()
const bodyParser = require('body-parser')


// getting books route
const bookRoute = require('./routes/bookRoute')


app.use(bodyParser.urlencoded({ extended: true }))
app.use(bodyParser.json())

// Setting url to access the routes  set by express
app.use('/books', bookRoute)


// Error Handling
app.use((req, res, next) => {
    const error = new Error('Data Not Found #Node')
    error.status = 404
    next(error)
})
app.use((error, req, res, next) => {
    res.status(error.status || 459)
    res.json({
        Error: {
            message: error.message
        }
    })
})


// Exporting the app for testing purpose and using in the server
module.exports = app