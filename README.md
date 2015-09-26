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