#!/usr/bin/node

// Reverse a list

exports.esrever = function (list) {
	let new_list = [];
	let list_length = list.length;
	for (let index = 0; index < list_length; index++) {
		new_list.push(list.pop());
	}
	return new_list;
};
