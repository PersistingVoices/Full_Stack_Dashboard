class Pinfo(models.Model):
	prj_name = models.CharField(max_length=255)
	prj_number= models.CharField(max_length=255)
	prj_manager= models.CharField(max_length=255)
	# def __str__(self):
	# 	return self.prj_name

class Reporting(models.Model):
	profit_centre = models.CharField(max_length=255)
	entity = models.CharField(max_length=255)
	app_centre= models.CharField(max_length=255)
	activity= models.CharField(max_length=255)
	report = models.CharField(max_length=255)
	# def __str__(self):
	# 	return self.prj_name

class Backlog(models.Model):
	revenue_backlog = models.FloatField()
	cost_to_go = models.FloatField()
	backlog_margin= models.FloatField()

class PS1(models.Model):
	as_sold_revenue = models.FloatField()
	as_sold_cost = models.FloatField()
	as_sold_margin_cost = models.FloatField()
	ps1_margin_lgm = models.FloatField()

class PS4(models.Model):
	as_sold_revenue = models.FloatField()
	as_sold_cost = models.FloatField()
	as_sold_margin_cost = models.FloatField()
	ps4_margin_lgm = models.FloatField()

class Actuals(models.Model):
	actual_cost = models.IntegerField()
	recognised_revenue_otd = models.IntegerField()
	invoice_revenue_otd = models.IntegerField()
	actual_cost_otd = models.IntegerField()
	recognised_revenue_ytd = models.IntegerField()
	invoice_revenue_ytd = models.FloatField()

class Payment(models.Model):
	cash_in = models.IntegerField()
	excess_billing = models.IntegerField()
	overdue = models.IntegerField()
	c_minus_i = models.IntegerField()
	i_minus_r = models.IntegerField()
	c_minus_r_percentage = models.FloatField()

class Slippages(models.Model):
	slippage_ps4_minus_ps1 = models.IntegerField()

class CPO(models.Model):
	merec_catalog = models.CharField()
	rel_score = models.IntegerField()
	rel_category = models.IntegerField()
	corporate_database = models.CharField(max_length=255)