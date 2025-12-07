(defun is-neighbor (cell)
  (and cell (char= cell #\@)))

(defun count-neighbors (row col grid)
  "Define all checkable directions, check neighbors in all of them."
  (let ((directions '((-1 . -1)
                      (0  . -1)
                      (1  . -1)
                      (-1 . 0)
                      (1  . 0)
                      (-1 . 1)
                      (0  . 1)
                      (1  . 1))))

    (count t
	   (mapcar (lambda (dir)
		     (let* ((r (+ row (car dir)))					
			    (c (+ col (cdr dir)))
			    (neighbor (if (and (>= r 0) (< r (length grid))
					       (>= c 0) (< c (length (car grid))))
					  (char (nth r grid) c)
					  nil)))
		     (is-neighbor neighbor)))
		   directions))))

(defun read-file-into-grid (filename)
  "Read a text file into a list of strings (rows)."
  (with-open-file (in filename)
    (loop for line = (read-line in nil)
          while line
          collect line)))

(defun has-less-than-four-neighbors (row col grid)
  "Check we are on an @ symbol, count neighbours when it's the case."
  (and (char= (char (nth row grid) col) #\@)
       (< (count-neighbors row col grid) 4)))

(defun count-removable-rolls (grid)
  "Count all @ symbols in the grid with fewer than 4 neighbors."
  (count t
         (mapcan (lambda (row row-index)
                   (map 'list (lambda (col col-index)
				(has-less-than-four-neighbors row-index col-index grid))
                        row
                        (loop for i from 0 below (length row) collect i)))
                 grid
                 (loop for i from 0 below (length grid) collect i))))

(setq grid (read-file-into-grid "input.txt"))
(count-removable-rolls grid)
