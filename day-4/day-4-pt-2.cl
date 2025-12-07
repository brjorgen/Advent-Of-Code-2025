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

(defun has-less-than-four-neighbors (row col grid)
  "Check we are on an @ symbol, count neighbours when it's the case."
  (and (char= (char (nth row grid) col) #\@)
       (< (count-neighbors row col grid) 4)))

(defun read-file-into-grid (filename)
  "Read a text file into a list of strings (rows)."
  (with-open-file (in filename)
    (loop for line = (read-line in nil)
          while line
          collect line)))

(defun replace-char (string index new-char)
  "Return a copy of STRING with character at INDEX replaced by NEW-CHAR."
  (let ((copy (copy-seq string)))
    (setf (char copy index) new-char)
    copy))

(defun removable-roll-positions (grid)
  "Return a list of (row . col) for all removable @'s."
  (loop for row in grid
        for row-index from 0
        append
        (loop for c across row
              for col-index from 0
              when (has-less-than-four-neighbors row-index col-index grid)
                collect (cons row-index col-index))))

(defun remove-positions (grid positions)
  "Return a new grid with given positions replaced by '.'."
  (reduce
   (lambda (g pos)
     (let* ((row (car pos))
            (col (cdr pos))
            (line (nth row g))
            (new-line (replace-char line col #\.)))
       (replace g (list new-line) :start1 row :end1 (1+ row))))
   positions
   :initial-value grid))

;; ooo fancy &
(defun remove-all-rolls (grid &optional (removed 0))
  "Remove all removable @'s until we can't anymore. Returns final grid and total removed rolls (two values)"
  (let ((positions (removable-roll-positions grid)))
    (if (null positions)
        (values grid removed)
        (remove-all-rolls
         (remove-positions grid positions)
         (+ removed (length positions))))))

(defun count-removable-rolls (grid)
  "Count all @ symbols in the grid with fewer than 4 neighbors."
  (length (removable-roll-positions grid)))

(setq grid (read-file-into-grid "input.txt"))
(count-removable-rolls grid)

(multiple-value-bind (final-grid total-removed)
    (remove-all-rolls grid)
  total-removed)
