#from jsonschema import validate
import jsonschema

# A sample schema, like what we'd get from json.load()
schema = {
	"type" : "object",
	"properties" : {
		"price" : {"type" : "number"},
		"name" : {"type" : "string"},
	},
        "required": ["name"]
}

# If no exception is raised by validate(), the instance is valid.
try:
    jsonschema.validate({"name" : "Eggs", "price" : 34.99}, schema)
    print("This is Valid JSON")
except jsonschema.ValidationError as e:
    print e.message
except jsonschema.SchemaError as e:
    print e
