#!/usr/bin/node

// Class Rectangle

class Rectangle {
	constructor (w, h) {
		if ((w > 0) && (h > 0)) {
			this.width = w;
			this.height = h;
		}
	}

	print () {
		for (let y = 0; y < this.height; y ++) {
			let display = '';
			for (let x = 0; x < this.width; x++) {
				display += 'x';
			}
			console.log(display);
		}
	}
}

module.exports = Rectangle;
