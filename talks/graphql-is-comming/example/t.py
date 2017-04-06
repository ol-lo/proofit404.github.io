from taskmanager.schema import schema

print('\n#1\n')
r = schema.execute('''
query {
  tasks {
    title
  }
}
''')
print(r.data)
print(r.errors)

print('\n#2\n')
r = schema.execute('''
query {
  task(id: "VGFzazox") {
    title
  }
}
''')
print(r.data)
print(r.errors)

print('\n#3\n')
r = schema.execute('''
query {
  allTasks {
    edges {
      node {
        id
        title
      }
    }
  }
}
''')
print(r.data)
print(r.errors)

print('\n#4\n')
r = schema.execute('''
query {
  allTasks(title_Startswith: "to") {
    edges {
      node {
        id
        title
      }
    }
  }
}
''')
print(r.data)
print(r.errors)
