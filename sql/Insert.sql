INSERT INTO public.tema2_user(
	id, name, lastname, social_security, age, address)
	VALUES (1, 'pedro', 'perales', 495787564, 23, 'casita abajo');
INSERT INTO public.tema2_user(
	id, name, lastname, social_security, age, address)
	VALUES (2, 'pedroncio', 'perales', 496787464, 23, 'casita abajo');
INSERT INTO public.tema2_user(
	id, name, lastname, social_security, age, address)
	VALUES (3, 'pedrito', 'perales', 495788464, 23, 'casita abajo');
INSERT INTO public.tema2_user(
	id, name, lastname, social_security, age, address)
	VALUES (4, 'paul', 'perales', 495797464, 23, 'casita abajo');
	
INSERT INTO public.tema2_login(
	id, email, password, created_at, updated_at, fk_user_id_id)
	VALUES (1, 'mail1@gmail.com', 'pass1', '2020-12-01', '2020-12-01', 1);
INSERT INTO public.tema2_login(
	id, email, password, created_at, updated_at, fk_user_id_id)
	VALUES (2, 'mail2@gmail.com', 'pass2', '2020-12-01', '2020-12-01', 2);
INSERT INTO public.tema2_login(
	id, email, password, created_at, updated_at, fk_user_id_id)
	VALUES (3, 'mail3@gmail.com', 'pass3', '2020-12-01', '2020-12-01', 3);
INSERT INTO public.tema2_login(
	id, email, password, created_at, updated_at, fk_user_id_id)
	VALUES (4, 'mail4@gmail.com', 'pass4', '2020-12-01', '2020-12-01', 4);
	
INSERT INTO public.tema2_invoice(
	id, sub_total, tax, total, billing_name, billing_identification, billing_address, created_at, updated_at)
	VALUES (1, 100, 10, 110, 'bill1', 1, 'address 1', '2020-12-01', '2020-12-01');
INSERT INTO public.tema2_invoice(
	id, sub_total, tax, total, billing_name, billing_identification, billing_address, created_at, updated_at)
	VALUES (2, 200, 0, 220, 'bill2', 2, 'address 1', '2020-12-01', '2020-12-01');
INSERT INTO public.tema2_invoice(
	id, sub_total, tax, total, billing_name, billing_identification, billing_address, created_at, updated_at)
	VALUES (3, 300, 30, 330, 'bill3', 3, 'address 1', '2020-11-01', '2020-11-01');
INSERT INTO public.tema2_invoice(
	id, sub_total, tax, total, billing_name, billing_identification, billing_address, created_at, updated_at)
	VALUES (4, 400, 40, 440, 'bill4', 4, 'address 1', '2021-01-01', '2021-01-01');
	
INSERT INTO public.tema2_purchases(
	id, payment_method, created_at, updated_at, fk_invoice_id_id, fk_user_id_id)
	VALUES (1, 'paypal', '2020-12-01', '2020-12-01', 1, 1);
INSERT INTO public.tema2_purchases(
	id, payment_method, created_at, updated_at, fk_invoice_id_id, fk_user_id_id)
	VALUES (2, 'paypal', '2020-12-01', '2020-12-01', 2, 2);
INSERT INTO public.tema2_purchases(
	id, payment_method, created_at, updated_at, fk_invoice_id_id, fk_user_id_id)
	VALUES (3, 'paypal', '2020-11-01', '2020-11-01', 3, 3);
INSERT INTO public.tema2_purchases(
	id, payment_method, created_at, updated_at, fk_invoice_id_id, fk_user_id_id)
	VALUES (4, 'cash', '2021-01-01', '2021-01-01', 4, 4);
	
INSERT INTO public.tema2_product(
	id, name, description, provider, price, quantity, created_at, updated_at)
	VALUES (1,'producto 1','descripcion 1', 'proveedor 1', 1, 10, '2020-11-01', '2020-11-01');
INSERT INTO public.tema2_product(
	id, name, description, provider, price, quantity, created_at, updated_at)
	VALUES (2,'producto 2','descripcion 2', 'proveedor 2', 2, 20, '2020-11-01', '2020-11-01');
INSERT INTO public.tema2_product(
	id, name, description, provider, price, quantity, created_at, updated_at)
	VALUES (3,'producto 3','descripcion 3', 'proveedor 3', 3, 30, '2020-11-01', '2020-11-01');
INSERT INTO public.tema2_product(
	id, name, description, provider, price, quantity, created_at, updated_at)
	VALUES (4,'producto 4','descripcion 4', 'proveedor 4',4, 40, '2020-11-01', '2020-11-01');
INSERT INTO public.tema2_product(
	id, name, description, provider, price, quantity, created_at, updated_at)
	VALUES (5,'producto 5','descripcion 5', 'proveedor 5', 5, 50, '2020-11-01', '2020-11-01');
INSERT INTO public.tema2_product(
	id, name, description, provider, price, quantity, created_at, updated_at)
	VALUES (6,'producto 6','descripcion 6', 'proveedor 6', 6, 60, '2020-11-01', '2020-11-01');
INSERT INTO public.tema2_product(
	id, name, description, provider, price, quantity, created_at, updated_at)
	VALUES (7,'producto 7','descripcion 7', 'proveedor 7', 7, 70, '2020-11-01', '2020-11-01');
INSERT INTO public.tema2_product(
	id, name, description, provider, price, quantity, created_at, updated_at)
	VALUES (8,'producto 8','descripcion 8', 'proveedor 8', 8, 80, '2020-11-01', '2020-11-01');
	
INSERT INTO public.tema2_invoiceproduct(
	id, created_at, updated_at, fk_invoice_id_id, fk_product_id_id)
	VALUES (1, '2020-12-01', '2020-12-01', 1, 1);
INSERT INTO public.tema2_invoiceproduct(
	id, created_at, updated_at, fk_invoice_id_id, fk_product_id_id)
	VALUES (2, '2020-12-01', '2020-12-01', 1, 2);
INSERT INTO public.tema2_invoiceproduct(
	id, created_at, updated_at, fk_invoice_id_id, fk_product_id_id)
	VALUES (3, '2020-12-01', '2020-12-01', 2, 3);
INSERT INTO public.tema2_invoiceproduct(
	id, created_at, updated_at, fk_invoice_id_id, fk_product_id_id)
	VALUES (4, '2020-12-01', '2020-12-01', 2, 4);
INSERT INTO public.tema2_invoiceproduct(
	id, created_at, updated_at, fk_invoice_id_id, fk_product_id_id)
	VALUES (5, '2020-11-01', '2020-11-01', 3, 5);
INSERT INTO public.tema2_invoiceproduct(
	id, created_at, updated_at, fk_invoice_id_id, fk_product_id_id)
	VALUES (6, '2020-11-01', '2020-11-01', 3, 6);
INSERT INTO public.tema2_invoiceproduct(
	id, created_at, updated_at, fk_invoice_id_id, fk_product_id_id)
	VALUES (7, '2021-01-01', '2021-01-01', 4, 7);
INSERT INTO public.tema2_invoiceproduct(
	id, created_at, updated_at, fk_invoice_id_id, fk_product_id_id)
	VALUES (8, '2021-01-01', '2021-01-01', 4, 8);