require 'sinatra'
require 'coffee-script'

TAKEN_USERNAMES = ['karoun', 'chanind', 'asuth', 'rdeaton', 'spiderman']

get '/coffee/app.coffee' do
  coffee :app
end

get '/' do
  erb :index
end

get '/signup' do
  erb :signup, :locals => {:errors => []}
end

post '/signup' do

  errors = validate_signup(params)

  if has_errors?(errors)
    erb :signup, :locals => {:errors => errors}
  else
    redirect to('/done')
  end
end

get '/done' do
  erb :done
end

def has_errors?(errors)
  errors.size > 0
end

def validate_signup(params)
  errors = []

  entered_username = params[:username] && params[:username] != ""
  entered_email = params[:email] && params[:email] != ""
  entered_password = params[:password] && params[:password] != ""

  errors << 'That username is already taken' if TAKEN_USERNAMES.include?(params[:username])
  errors << 'You must enter a username' unless entered_username
  errors << 'Your username must be at least 2 characters' if params[:username].size < 2 && entered_username
  errors << 'Your username must be at most 20 characters' if params[:username].size > 20
  errors << 'Your username must contain only letters, number, and underscores' unless params[:username] =~ /^[a-zA-Z0-9_]+$/

  errors << 'You must enter an email' unless entered_email
  errors << 'Invalid email' unless !entered_email || params[:email] =~ /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/

  errors << 'You must enter a password' unless entered_password
  errors << 'You password must be at least 6 characters long' if entered_password && params[:password].size < 6

  errors << "Your passwords don't match" if params[:password] != params[:password_repeat]

  errors << "You must accept the terms of service" if params[:tos] != 'agree'

  return errors
end
