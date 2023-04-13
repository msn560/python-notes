['height', 'width'].forEach(property => {
    // store the existing descriptor
    const imageDescriptor = Object.getOwnPropertyDescriptor(HTMLImageElement.prototype, property);

    // redefine the property with a patched descriptor
    Object.defineProperty(HTMLImageElement.prototype, property, {
        ...imageDescriptor,
        get: function () {
            // return an arbitrary non-zero dimension if the image failed to load
            if (this.complete && this.naturalHeight == 0) {
                return 20;
            }
            // otherwise, return the actual dimension
            return imageDescriptor.get.apply(this);
        },
    });
});
// store the existing descriptor
const elementDescriptor = Object.getOwnPropertyDescriptor(HTMLElement.prototype, 'offsetHeight');

// redefine the property with a patched descriptor
Object.defineProperty(HTMLDivElement.prototype, 'offsetHeight', {
    ...elementDescriptor,
    get: function () {
        if (this.id === 'modernizr') {
            return 1;
        }
        return elementDescriptor.get.apply(this);
    },
});