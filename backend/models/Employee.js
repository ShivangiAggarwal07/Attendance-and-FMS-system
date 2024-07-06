const mongoose = require('mongoose');

const employeeSchema = new mongoose.Schema({
  firstName: { type: String, required: true },
  lastName: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  designation: { type: String, required: true },
  birthDate: { type: Date, required: true },
  gender: { type: String, required: true },
  phoneNumber: { type: String, required: true },
  address: { type: String, required: true },
  city: { type: String, required: true },
  state: { type: String, required: true },
  country: { type: String, required: true },
  education: { type: String, required: true },
  experience: { type: String, required: true },
  skills: [{ type: String }],
  photo: { type: String, required: true }
});

module.exports = mongoose.model('Employee', employeeSchema);