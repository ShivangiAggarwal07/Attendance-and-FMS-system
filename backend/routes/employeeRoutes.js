const express = require('express');
const router = express.Router();
const Employee = require('../models/Employee');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
// const bcrypt = require('bcrypt');

// Ensure the uploads directory exists
const uploadDir = path.join(__dirname, '..', 'uploads');
if (!fs.existsSync(uploadDir)) {
  fs.mkdirSync(uploadDir);
}

// Set up multer for file upload with file format restrictions
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, uploadDir);
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + path.extname(file.originalname));
  }
});

const fileFilter = (req, file, cb) => {
  const filetypes = /jpeg|jpg|png/;
  const extname = filetypes.test(path.extname(file.originalname).toLowerCase());
  const mimetype = filetypes.test(file.mimetype);

  if (mimetype && extname) {
    return cb(null, true);
  } else {
    cb('Error: Images Only!');
  }
};

const upload = multer({ 
  storage: storage,
  fileFilter: fileFilter
});

// Async error handling middleware
const asyncHandler = fn => (req, res, next) => {
  Promise.resolve(fn(req, res, next)).catch(next);
};

// POST route to create a new employee
router.post('/postdata', upload.single('photo'), asyncHandler(async (req, res) => {
  console.log('Received request body:', req.body);
  console.log('Received file:', req.file);

  if (!req.file) {
    return res.status(400).json({ message: 'Photo is required' });
  }

  // Extract required fields from the request body
  const {
    firstName,
    lastName,
    email,
    password,
    designation,
    birthDate,
    gender,
    phoneNumber,
    address,
    city,
    state,
    country,
    education,
    experience,
    skills
  } = req.body;

  // Log the type of skills to debug the issue
  console.log('Type of skills:', typeof skills);

  // Validate all required fields are present
  if (
    !firstName || !lastName || !email || !password || !designation ||
    !birthDate || !gender || !phoneNumber || !address || !city ||
    !state || !country || !education || !experience
  ) {
    return res.status(400).json({ message: 'All fields are required' });
  }

  //   Hash the password
  //  const hashedPassword = await bcrypt.hash(password, 10);

  const employeeData = {
    firstName,
    lastName,
    email,
    password,  // password: hashedPassword
    designation,
    birthDate,
    gender,
    phoneNumber,
    address,
    city,
    state,
    country,
    education,
    experience,
    photo: req.file.path,
    skills: typeof skills === 'string' ? skills.split(',') : []
  };

  const employee = new Employee(employeeData);
  await employee.save();
  console.log('Employee Data:', employeeData);

  res.status(201).json({ message: 'Employee registered successfully', employee });
}));

// GET route to fetch all employees
router.get('/', asyncHandler(async (req, res) => {
  const employees = await Employee.find();
  res.json(employees);
}));

// Error handling middleware
router.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Internal Server Error', error: err.message });
});

module.exports = router;



//LOGIN ROUTE

// router.post('/login', asyncHandler(async (req, res) => {
//   const { email, password } = req.body;

//   const employee = await Employee.findOne({ email });
//   if (!employee) {
//     return res.status(400).json({ message: 'Invalid email or password' });
//   }

//   const isMatch = await bcrypt.compare(password, employee.password);
//   if (!isMatch) {
//     return res.status(400).json({ message: 'Invalid email or password' });
//   }

//   res.status(200).json({ message: 'Login successful', employee });
// }));
