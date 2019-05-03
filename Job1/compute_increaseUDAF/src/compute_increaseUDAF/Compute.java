package compute_increaseUDAF;


import java.text.ParseException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.apache.hadoop.hive.common.type.Date;
import org.apache.hadoop.hive.ql.exec.UDAF;
import org.apache.hadoop.hive.ql.exec.UDAFEvaluator;
import org.apache.hadoop.hive.ql.metadata.HiveException;


/*There are three kind of UDFs in Hive:
											1.Regular UDF, 
											2.User Defined Aggregate Function (UDAF),  
											3.User Defined Tabular Function (UDTF).

UDFs works on a single row in a table and produces a single row as output. 
Its one to one relationship between input and output of a function. e.g Hive built in TRIM() function.

UDAF:  User defined aggregate functions works on more than one row and gives single row as output. 
e.g Hive built in MAX() or COUNT() functions.

We need to overwrite five methods called init(), iterate(), terminatePartial(), merge() and terminate() in our class. 

init() – This method initializes the evaluator and resets its internal state. 
iterate() – This method is called every time there is a new value to be aggregated. The evaluator should update its internal state with the result of performing the aggregation (we are doing sum – see below). We return true to indicate that the input was valid.
terminatePartial() – This method is called when Hive wants a result for the partial aggregation. The method must return an object that encapsulates the state of the aggregation.
merge() – This method is called when Hive decides to combine one partial aggregation with another.
terminate() – This method is called when the final result of the aggregation is needed.


UDTF:  User defined tabular function works on one row as input and returns multiple rows as output. So here the relation in one to many. 
e.g Hive built in EXPLODE() function. 

from: https://www.linkedin.com/pulse/hive-functions-udfudaf-udtf-examples-gaurav-singh

 */


@SuppressWarnings("deprecation")
public class Compute extends UDAF{

	public static class PercentageUDAFEvaluator implements UDAFEvaluator{

		static final Log LOG = LogFactory.getLog(PercentageUDAFEvaluator.class.getName());

		private HashMap<Date, Double> elements;

		public PercentageUDAFEvaluator() {
			super();
			init();
		}

		public void init() {
			LOG.debug("======== init ========");
			elements = new HashMap<Date, Double>();
		}

		public boolean iterate(String data, double value) throws HiveException, ParseException {
			LOG.debug("======== iterate ========");

			if (elements == null)
				throw new HiveException("Item is not initialized");

			Date time = Date.valueOf(data); 
			elements.put(time, value);
			return true;
		}

		public HashMap<Date, Double> terminatePartial() {
			LOG.debug("======== terminatePartial ========");
			return elements;
		}


		public boolean merge(HashMap<Date,Double> other) {
			LOG.debug("======== merge ========"); 
			elements.putAll(other);
			return true;
		}

		public double terminate(){
			LOG.debug("======== terminate ========");

			ArrayList<Date> lista = new ArrayList<>();
			lista.addAll(elements.keySet());
			double chiave_min = elements.get(Collections.min(lista));

			ArrayList<Date> lista1 = new ArrayList<>();
			lista1.addAll(elements.keySet());
			Double chiave_max = elements.get(Collections.max(lista1));

			double b = chiave_min;
			double a = chiave_max;	

			double perc = ((100*(b-a))/a);   

			return perc;
		}
	}

	public static void main(String[] args) throws HiveException, ParseException {

		// set up the models we need
		PercentageUDAFEvaluator example = new PercentageUDAFEvaluator();
		PercentageUDAFEvaluator example1 = new PercentageUDAFEvaluator();

		double a = 6.78;
		double b = 5.78;
		double c = 4.68;
		double d = 4.78;

		String prima = "2017-02-05";
		String p = "2017-02-05";
		String s = "2014-02-05";
		String m = "2015-12-05";
		String n = "2016-06-05";
		String k = "2017-05-05";
		String l = "2019-04-05";
		String q = "1998-03-05";

		double e =10.78;
		double f =12.78;
		double g =21.68;
		double h =14.78;

		example.init();

		example1.init();

		example.iterate(prima,a);
		example.iterate(p,b);
		example.iterate(s,c);
		example.iterate(m,d);

		example1.iterate(n,e);
		example1.iterate(k,h);
		example1.iterate(l,f);
		example1.iterate(q,g);

		System.out.println(example.terminatePartial());

		example.merge(example1.terminatePartial());

		System.out.println(example.terminatePartial());

		System.out.println(example.terminate());
	}
}