import jsonschema
import simplejson

with open('PersonSchema.json', 'r') as f:
    schema_data = f.read()
    schema = simplejson.loads(schema_data)

with open('Person.json', 'r') as f:
    sample_data = f.read()
    sample = simplejson.loads(sample_data)

# If no exception is raised by validate(), the instance is valid.
try:
    jsonschema.validate(sample, schema)
    print("This is Valid JSON")
except jsonschema.ValidationError as e:
    print e.message
except jsonschema.SchemaError as e:
    print e
