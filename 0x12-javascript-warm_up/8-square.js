#!/usr/bin/node
const arg = process.argv[2];

if (!isNaN(arg) && Number.isInteger(parseFloat(arg))) {
    const size = parseInt(arg);
    if (size <= 0) {
        console.log("Invalid size");
    } else {
        const row = "X".repeat(size);
        for (let i = 0; i < size; i++) {
            console.log(row);
        }
    }
} else {
    console.log("Missing size");
}
