const chai = require('chai')
const chai_http = require('chai-http')
const app = require('../app')

// configure chai

chai.use(chai_http)
chai.should()

describe('Books', () => {
    describe('GET/ ', () => {
        // Test to get all the books
        it('it should fetch all the books', (done) => {
            chai.request(app)
                .get('/books')
                .end((err, res) => {
                    res.should.have.status(200)
                    res.body.should.be.a('object')

                    done()
                })
        })

        // Test to get a single record
        it('it should fetch a certain book', (done) => {
            chai.request(app)
                .get(`/books/${1001}`)
                .end((err, res) => {
                    res.should.have.status(200)

                    res.body.should.have.property('Book')
                    res.body.Book.should.have.property('id')
                    res.body.Book.should.have.property('title')
                    res.body.Book.should.have.property('author')
                    done()
                })

        })

        // Test if the book is not found and error is sent as response
        it('it should throw error if the book is not found', (done) => {
            chai.request(app)
                .get(`/books/${1010}`)
                .end((err, res) => {
                    res.should.have.status(404)
                    res.body.should.have.property('message').eql('Book Not Found')
                    done()
                })

        })

    })

    describe('/POST', () => {

        // Test to add a book in the list
        it('it should add a book in the file', (done) => {
            const book = {
                id: "1005",
                title: "Harry Potter",
                author: "J.K Rowling"
            }
            chai.request(app)
                .post('/books')
                .send(book)
                .end((err, res) => {
                    res.should.have.status(200)
                    res.body.should.have.property('message').eql('Successfully Added Book')
                    done()
                })
        })

        // Test to if the book being added doesnt have all the required properties
        it('it should throw error when added incomplete details of book', (done) => {
            const book = {
                id: "1006",
                title: "Harry Potter"
            }
            chai.request(app)
                .post('/books')
                .send(book)
                .end((err, res) => {
                    res.should.have.status(404)
                    res.body.should.have.property('message').eql('Failed to post book')
                    res.body.should.have.property('Error').eql('Object Not Completely Defined')
                    done()
                })
        })


    })

    describe('/DELETE', () => {

        // it should delete the book
        it('it should delete the book', (done) => {
            chai.request(app)
                .delete(`/books/delete/${1005}`)
                .end((err, res) => {
                    res.should.have.status(200)
                    res.body.should.have.property('message').eql('Successfully Deleted Book')
                    done()
                })
        })

    })


})