#!/usr/bin/node

module.exports = class Rectangle {
	constructor (w, h) {
	  if (w <= 0 || h <= 0) {
		return 0;
	  } else if (!w || !h) {
		return 0;
	  }
	  this.width = w;
	  this.height = h;
	}
  
	print () {
	  let size;
	  let j;
  
	  for (size = 0; size < this.height; size++) {
		let row = '';
		for (j = 0; j < this.width; j++) {
		  row += 'X';
		}
		console.log(row);
	  }
	}

	rotate () {
	  let temp;

	  temp = this.height;
	  this.height = this.width;
	  this.width = temp;
	}

	double () {
		this.width = this.width * 2;
		this.height = this.height * 2;
	}
  };
  