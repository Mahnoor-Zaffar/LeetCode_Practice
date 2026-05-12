/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function (obj) {
    if (typeof obj !== 'object' || obj == null) {
        return obj
    }
    const isArray = Array.isArray(obj)
    const result = Array.isArray(obj) ? [] : {}
    const keys = Object.keys(obj)
    for (const key of keys) {
        let value = obj[key]
        let compactedValue = compactObject(value)
        if (Boolean(compactedValue)) {
            if (isArray) {
                result.push(compactedValue)
            } else {
                result[key] = compactedValue
            }
        }
    }
    return result
};