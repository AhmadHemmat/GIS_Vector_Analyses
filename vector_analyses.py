from osgeo import ogr


class VectorAnalyse:
    def __init__(self, target_vector_param, output_vector_param, factors_param):
        self.target_vector = target_vector_param
        self.output_vector = output_vector_param
        self.factors = factors_param
    
    def driver(self):
        driver_name = "ESRI shapefile"
        driver = ogr.GetDriverByName(driver_name)
        return driver
    
    def input_target(self, driver):
        in_data_source = driver.Open(self.target_vector, 0)
        return in_data_source
    
    def input_layer(self, in_data_source):
        in_layer = in_data_source.GetLayer()
        return in_layer
    
    def output(self, driver):
        out_data_source = driver.CreateDataSource(self.output_vector)
        return out_data_source
    
    def out_layer(self, out_data_source):
        out_layer = out_data_source.CreateLayer('FINAL', geom_type=ogr.wkbMultiPolygon)
        return out_layer
    
    def input_factor(self, driver):
        in_factor_source = driver.Open(self.factors['factor'], 0)
        return in_factor_source
    
    def input_factor_layer(self, in_factor_source):
        in_factor_layer = in_factor_source.GetLayer()
        return in_factor_layer  
    
    def initial(self, in_data_source, out_data_source, input_factor_source):
        in_layer = self.input_layer(in_data_source)
        out_layer = self.out_layer(out_data_source)
        input_factor_layer = self.input_factor_layer(input_factor_source)
        io = {
            'in_layer': in_layer, 
            'out_layer': out_layer, 
            'input_factor_layer': input_factor_layer
        } 
        return io 
    
    def run(self):
        pass

class ClipVector(VectorAnalyse):
    def clip(self, in_layer, input_factor_layer, out_layer):
        ogr.Layer.Clip(in_layer, input_factor_layer, out_layer)
    def run(self):
        driver = super().driver()
        in_data_source = super().input_target(driver)
        out_data_source = super().output(driver)
        input_factor_source = super().input_factor(driver)

        initial = super().initial(in_data_source, out_data_source, input_factor_source)
        self.clip(initial['in_layer'], initial['input_factor_layer'], initial['out_layer'])

        in_data_source.Destroy()
        input_factor_source.Destroy()
        out_data_source.Destroy()

class UnionVector(VectorAnalyse):
    def union(self, in_layer, input_factor_layer, out_layer):
        ogr.Layer.Union(in_layer, input_factor_layer, out_layer)
    def run(self):
        driver = super().driver()
        in_data_source = super().input_target(driver)
        out_data_source = super().output(driver)
        input_factor_source = super().input_factor(driver)

        initial = super().initial(in_data_source, out_data_source, input_factor_source)
        self.union(initial['in_layer'], initial['input_factor_layer'], initial['out_layer'])

        in_data_source.Destroy()
        input_factor_source.Destroy()
        out_data_source.Destroy()

class EraseVector(VectorAnalyse):
    def erase(self, in_layer, input_factor_layer, out_layer):
        ogr.Layer.Erase(in_layer, input_factor_layer, out_layer)
    def run(self):
        driver = super().driver()
        in_data_source = super().input_target(driver)
        out_data_source = super().output(driver)
        input_factor_source = super().input_factor(driver)

        initial = super().initial(in_data_source, out_data_source, input_factor_source)
        self.erase(initial['in_layer'], initial['input_factor_layer'], initial['out_layer'])

        in_data_source.Destroy()
        input_factor_source.Destroy()
        out_data_source.Destroy()

class IntersectionVector(VectorAnalyse):
    def intersection(self, in_layer, input_factor_layer, out_layer):
        ogr.Layer.Intersection(in_layer, input_factor_layer, out_layer)
    def run(self):
        driver = super().driver()
        in_data_source = super().input_target(driver)
        out_data_source = super().output(driver)
        input_factor_source = super().input_factor(driver)

        initial = super().initial(in_data_source, out_data_source, input_factor_source)
        self.intersection(initial['in_layer'], initial['input_factor_layer'], initial['out_layer'])

        in_data_source.Destroy()
        input_factor_source.Destroy()
        out_data_source.Destroy()