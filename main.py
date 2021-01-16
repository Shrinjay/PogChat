import sqlalchemy as sql
import flask as f
import cockroachdb as cd

# Define endpoint routes and begin implementing:
# For now lets define a get route to get all messages for a certain location
# And a post route to add messages to the DB.
# DB schema will be as discussed, hold userid, messages join and coordinates.
# Send and recieve as JSONs, client side will convert into message objects

