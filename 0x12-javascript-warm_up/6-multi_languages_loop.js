#!/usr/bin/node
const c = 'C is fun';
const python = 'Python is cool';
const java = 'Javascript is amazing';
const array = [c, python, java];
for (let i in array)
{
    console.log(array[i]);
}