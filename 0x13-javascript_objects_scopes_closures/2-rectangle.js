#!/usr/bin/node
class Rectangle {
    constructor(w, h) {
        if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
            // Create an empty object if w or h is equal to 0 or not a positive integer
            return {};
        }
        this.width = w;
        this.height = h;
    }
}
