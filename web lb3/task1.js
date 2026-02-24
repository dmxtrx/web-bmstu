function parseCSVLine(line) {
    const fields = [];
    let current = '';
    let inQuotes = false;
    for (let char of line) {
        if (char === '"' && !inQuotes) {inQuotes = true;} 
        else if (char === '"' && inQuotes) {inQuotes = false;} 
        else if (char === ',' && !inQuotes) {fields.push(current); current = '';}
        else {current += char;}
    }
    fields.push(current);
    return fields;
}

function parseCSV(text) {
    const lines = text.split('\n');
    const headers = parseCSVLine(lines[0]);
    const result = [];
    for (let i = 1; i < lines.length; i++) {
        if (lines[i].trim() === '') continue;
        const values = parseCSVLine(lines[i]);
        const obj = {};
        for (let j = 0; j < headers.length; j++) {
            obj[headers[j]] = values[j];
        }
        result.push(obj);
    }
    return result;
}