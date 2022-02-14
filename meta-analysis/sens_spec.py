class DiagnosticTestMetrics():

    def __init__(self, tp, fp, tn, fn):
        
        self.tp = tp
        self.fp = fp
        self.tn = tn
        self.fn = fn

    @property
    def sensitivity(self):
        self._sensitivity = self.tp / (self.tp + self.fn)
        return(self._sensitivity)        

    @property
    def specificity(self):
        self._specificity = self.tn / (self.tn + self.fp)
        return(self._specificity)        

    @property
    def ppv(self):
        self._ppv = self.tp / (self.tp + self.fp)
        return(self._ppv)        

    @property
    def npv(self):
        self._npv = self.tn / (self.tn + self.fn)
        return(self._npv)        


    @property
    def n_patients(self):
        self._n_patients = self.tp + self.fp + self.tn + self.fn
        return(self._n_patients)

    def summary(self):

        print('''
####################################
         Summary statistics 
####################################

''',

        'Total patients = ', self.n_patients,

        '\nSensitivity = ', self.sensitivity,

        '\nSpecificity= ', self.specificity
        )
