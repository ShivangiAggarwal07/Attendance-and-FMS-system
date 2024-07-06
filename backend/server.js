const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const bodyParser = require('body-parser');
const cors = require('cors');
const employeeRoutes = require('./routes/employeeRoutes');

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Apply CORS middleware before other middlewares
app.use(bodyParser.json());
app.use(cors({
    origin: ['http://127.0.0.1:5500']
}));


// Other middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log('Connected to MongoDB'))
.catch(err => console.error('Error connecting to MongoDB:', err));

// Routes
app.use('/routes/employees', employeeRoutes);

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});