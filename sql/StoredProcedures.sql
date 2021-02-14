CREATE OR REPLACE FUNCTION products_by_payment(month_arg date,payment_arg text, results_arg integer)
  RETURNS TABLE (product   varchar   
               , payment_method   varchar
               , created_at timestamptz) AS
$func$
BEGIN
   RETURN QUERY
   	select pr.name as product,
	pch.payment_method as payment_method,
	pch.created_at as created_at
	from tema2_product as pr
	INNER join tema2_invoiceproduct as ip on pr.id=ip.fk_product_id_id
	inner join tema2_invoice as inv on ip.fk_invoice_id_id=inv.id
	inner join tema2_purchases as pch on pch.fk_invoice_id_id=inv.id
	where pch.created_at=month_arg and pch.payment_method=payment_arg
	fetch first results_Arg rows only;                    
END
$func$  LANGUAGE plpgsql;

SELECT * FROM products_by_payment('2020-11-01','paypal',100);


CREATE OR REPLACE FUNCTION sales_no_tax(date_arg date, tax_arg integer)
  RETURNS TABLE (user_id integer, 
				 user_name text,
				 email varchar,
				amount decimal) AS
$func$
BEGIN
   RETURN QUERY
   	select usr.id as user_id,concat(usr.name,' ',usr.lastname) as user_name, lgn.email as email,sum(inv.total) as amount 
	from tema2_user as usr
	inner join tema2_login as lgn on lgn.fk_user_id_id=usr.id
	inner join tema2_purchases as pch on usr.id=pch.fk_user_id_id
	inner join tema2_invoice as inv on pch.fk_invoice_id_id=inv.id
	where extract(year from pch.created_at)=extract(year from date_arg) and inv.tax=tax_arg
	group by usr.id,lgn.email;                   
END
$func$  LANGUAGE plpgsql;

SELECT * FROM sales_no_tax('2020-11-01',0);



