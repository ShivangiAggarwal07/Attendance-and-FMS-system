const express = require('express');
const router = express.Router();
const Employee = require('../models/Employee');
const multer = require('multer');
const path = require('path');

// Set up multer for file upload
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, 'uploads/');
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + path.extname(file.originalname));
  }
});

const upload = multer({ storage: storage });

// POST route to create a new employee
router.post('/', upload.single('photo'), async (req, res) => {
  console.log('Received request body:', req.body);
  console.log('Received file:', req.file);
  try {
    const employeeData = {
      ...req.body,
      photo: req.file.path,
      skills: req.body.skills ? req.body.skills.split(',') : []
    };

    const employee = new Employee(employeeData);
    await employee.save();
    res.status(201).json({ message: 'Employee registered successfully', employee });
  } catch (error) {
    res.status(400).json({ message: 'Error registering employee', error: error.message });
  }
});

// GET route to fetch all employees
router.get('/', async (req, res) => {
  try {
    const employees = await Employee.find();
    res.json(employees);
  } catch (error) {
    res.status(500).json({ message: 'Error fetching employees', error: error.message });
  }
});

module.exports = router;
