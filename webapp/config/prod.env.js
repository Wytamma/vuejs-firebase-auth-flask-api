'use strict'
const FIREBASE_CONFIG = require('./firebase.config.json')

module.exports = {
  NODE_ENV: '"production"',
  FIREBASE_CONFIG: JSON.stringify(FIREBASE_CONFIG),
}
