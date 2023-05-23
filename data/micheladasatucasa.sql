
create table usuario(idUsuario int not null auto_increment primary key, nombres varchar (20), apellidoPaterno varchar (15),
					apellidoMaterno varchar (15),correo varchar (30),fechaNacimiento date, contrasena varchar (25),
                    calle varchar (20), numero int not null, cp int not null, colonia varchar (20), ciudad varchar (25),
                    estado varchar (20),tipoUsuario varchar(15));
                    
create table producto (idProducto int not null auto_increment primary key,  nombre varchar not null (20),
                       descripcion varchar not null (250), precio decimal(6,2) NOT NULL DEFAULT '9999.99',
                       cantidadInventario int not null);
                       
create table pedido (idPedido int not null auto_increment primary key, cantidad int not null, 
                     total decimal(6,2) NOT NULL DEFAULT '9999.99', estatus boolean, fecha date);
                     
create table insumo (idInsumo int not null auto_increment primary key,nombre varchar (25),cantidad int not null, fecha date);

create table atiende (id_pedido int not null, id_usuario int not null, foreign key (id_pedido) references pedido (idPedido),
                      foreign key (id_usuario) references usuario (idUsuario));
                      
create table ordena (id_pedido int not null, id_usuario int not null, foreign key (id_pedido) references pedido (idPedido),
                      foreign key (id_usuario) references usuario (idUsuario));
                      
create table agrega (id_usuario int not null, id_producto int not null, fecha date, cantidad int not null,  foreign key (id_usuario) 
					references usuario (idUsuario), foreign key (id_producto) references producto(idProducto));

create table registra (id_insumo int not null, id_usuario int not null, foreign key (id_usuario) references usuario (idUsuario),
                       foreign key (id_insumo) references insumo (idInsumo));  
                       
create table consume (id_producto int not null, id_insumo int not null, foreign key (id_producto) references producto(idProducto),
                      foreign key (id_insumo) references insumo (idInsumo));
                      
create table conforma (id_pedido int not null, id_producto int not null, foreign key (id_pedido) references pedido (idPedido),
                       foreign key (id_producto) references producto(idProducto));

                    
                    
                    
                    
                    
                    








 
