/**
 * Documentation: http://docs.azk.io/Azkfile.js
 */
// Adds the systems that shape your system
systems({
  demoapp: {
    // Dependent systems
    depends: ["db"],
    // More images:  http://images.azk.io
    image: {
      "dockerfile": "./containers/web/"
    },
    workdir: "/azk/#{manifest.dir}/code",
    shell: "/bin/bash",
    command: "python app.py",
    wait: 20,
    mounts: {
      '/azk/#{manifest.dir}': path("."),
    },
    scalable: {
      default: 2,
      limit: 28
    },
    http: {
      domains: [ "#{system.name}.#{azk.default_domain}" ],
    },
    ports: {
      // exports global variables
      http: "80/tcp",
    },
    envs: {
      // set instances variables
      EXAMPLE: "value",
      VIRTUAL_HOST: "demoapp.inet",
    },
  },

  db: {
    depends: [],
    image: {"docker": "azukiapp/mysql"},
    shell: "/bin/bash",
    wait: {"retry": 25, "timeout": 1000},
    mounts: {
      '/var/lib/mysql': persistent("mysql_lib#{system.name}"),
    },
    ports: {
      data: "3306:3306/tcp",
    },
    envs: {
      MYSQL_ROOT_PASSWORD: "123456",
      MYSQL_USER: "root",
      MYSQL_PASS: "123456",
      // MYSQL_DATABASE: "#{manifest.dir}_development",
      MYSQL_DATABASE: "demoapp",
    },
  },

});
