# Docker Demo Application

Aplicação utilizada para exemplificar o uso do docker


## Tags

 - V1 - aplicação monolitica
    - Antes de iniciar vamos ao path `/code` e rodamos `sqlite3 database.db < schema.sql` para criar a tabela no sqlite

 - V2 - aplicação monolitica persistindo em banco sqlite

 - V3 - aplicação consumindo MySQL de outro container
    - Devemos remover o container web `docker-compose rm web` e fazer rebuild do container web antes de rodar o docker-compose up
    - Após subir os containers vamos ao path `/code` e rodamos `mysql -h $(dmac ip curso) -uroot -p demoapp < schema.sql` para criar a tabela no mysql
 - V4 - Colocado proxy para suportar LB
    - adicionar 192.168.99.100  demoapp.inet no /etc/hosts
 - V5 - Colocado arquivo crane.yaml que define a orquestração usando a ferramenta Crane: [https://github.com/michaelsauter/crane](https://github.com/michaelsauter/crane)
    - adicionar 192.168.99.100  demoapp.inet no /etc/hosts
 - V6 - Colocado arquivo azkfile.js que define orquestração pelo AZK [http://www.azk.io/](http://www.azk.io/)
    - não é necessário a entrada no arqivo de hosts
    - Após subir os containers vamos ao path `/code` e rodamos `mysql -h db.inet  -uroot -p demoapp < schema.sql` para criar a tabela no mysql