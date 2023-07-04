const express = require('express')
const port = 3000
const app = express()
const path = require('path')
const pt = path.join(__dirname, 'vue-project','dist')
app.use(express.static(pt))
app.get("/", (req,res) => {
    res.sendFile(pt)
})
app.listen(process.env.PORT || port, () => {
    console.log(`Example app listening on port ${port}`)
})